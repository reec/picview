function PicView() {
    // So we don't have to worry about function scopes
    var self = this;

    // Frequently used persistent elements
    self.$body = $('body');
    self.$content = self.$body.find('#content');

    // -- Init method -- (should be run after instantiation and configuration)
    self.init = function() {
        // -- Listeners --
        // Click listener
        self.$body.on('click', 'a.ajax', self.click_handler);
        // popState listener
        $(window).on('popstate', self.popstate_handler);

        // Update the current state, so back button works
        self.replace_state();
    };

    // -- Other methods --
    self.request = function(url) {
        console.log('requesting', url);
        $.ajax({
            url         : url,
            dataType    : 'json'
        }).done(function(response_data, textStatus, jqXHR) {
            console.log('done');
            // Push a new state to history
            self.insert_html(response_data.html); // update the dom with the response data
            self.push_state(url, response_data.title); // mark this as a new place in history

        }).fail(function(jqXHR, textStatus, errorThrown) {
            alert(textStatus + ' ' + errorThrown);
        });
    };

    self.insert_html = function(html_parts) {
        for (var key in html_parts) {
            // It's good practice to filter out meta stuff even if we don't really need to
            if (!html_parts.hasOwnProperty(key)) {
                continue;
            }
            // '+#myid' --> append to #myid
            var selector = key;
            var append = false;
            if (key.charAt(0) == '+') {
                append = true;
                selector = key.substr(1);
            }
            var $el = self.$body.find(selector);
            if (append) {
                console.log('appending to ', selector);
                $el.append(html_parts[key]);
            } else {
                console.log('replacing content in ', selector);
                $el.html(html_parts[key]);
            }
        }
    };

     self.popstate_handler = function(e) {
        var state_data = e.originalEvent.state;
        console.log('popped state: ', state_data);
        if (state_data !== null) {
            self.apply_state(state_data);
        }
    };

    self.push_state = function(url, title) {
        // Push a new state to the history

        var state = self.build_state_object();
        state.title = title;
        console.log('pushing new state: ', state, 'title: ', title);
        window.history.pushState(state, 'ignored', url);
        // Since pushState is broken..
        document.title = title;
    };

    self.replace_state = function(url) {
        console.log('replacing state');
        if (url == undefined) {
            url = null;
        }
        window.history.replaceState(self.build_state_object(), 'ignored', url);
    };

    self.apply_state = function(state_object) {
        self.insert_html(state_object.html_parts);
        document.title = state_object.title;
    };

    self.build_state_object = function() {
        // This is the state object that is saved in the clients browser
        return {
            title           : document.title,
            html_parts      : {'#content': self.$content.html()}
        }
    };

    self.click_handler = function(e) {
        var $clicked_el = $(e.currentTarget);
        e.preventDefault();
        console.log('clicked on', $clicked_el);

        var href = $clicked_el.attr('href');
        if (href) {
            self.request(href);
        }
    };
}


$(function() {
    var picview = new PicView();
    window.picview = picview;
    picview.init();

    var $body = picview.$body;

    $body.on('click', '#view #image .nav-link#zoom', function() {
        $body.toggleClass('full-screen');
    });
});