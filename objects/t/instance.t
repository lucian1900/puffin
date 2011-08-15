$load 'rosella/test.pbc';
$load 'puffin/builtins.pbc';

class instance {
    function get_mro() {
        /* a, b, c, d are all classes
        Inheritance chain looks like this
        d
        | \
        b c
        \ |
         a
        */
        var a = new Python.instance;
        var b = new Python.instance;
        var c = new Python.instance;
        var d = new Python.instance;

        a.__name__ = 'a';
        b.__name__ = 'b';
        c.__name__ = 'c';
        d.__name__ = 'd';

        d.__bases__ = [];
        b.__bases__ = [d];
        c.__bases__ = [d];
        a.__bases__ = [b, c];

        using Python.get_mro;
        var mro = get_mro(a);
        
        self.assert.equal(mro, [a, b, c, d]);
    }

    function set_get_attr() {
        var i = new Python.instance;
        i.a = 2;

        self.assert.equal(i.a, 2);
    }

    function get_bases() {
        var i = new Python.instance;
        i.__bases__ = [1, 2];

        self.assert.equal(i.__bases__, [1, 2]);
    }

    function get_attr_override() {
        var i = new Python.instance;
        var c = new Python.instance;

        i.__class__ = c;

        c.__getattribute__ = function(obj, name) {
            return 42;
        };

        self.assert.equal(i.a, 42);
    }
    
    function set_attr_override() {
        var i = new Python.instance;
        var c = new Python.instance;

        i.__class__ = c;

        c.__setattr__ = function(obj, name, value) {
            obj.__dict__[name] = 42;
        };

        i.a = 2;

        self.assert.equal(i.a, 42);
    }

    function call_func() {
        var i = new Python.instance;
        i.b = function(){return 42;};

        var func = i.b;
        self.assert.equal(i.b(), 42);
    }

    function call_func_attr() {
        var i = new Python.instance;
        i.f = function(a, b){return a + b;};

        var func = i.f;
        self.assert.equal(i.f(1, 2), 3);
    }

    function get_string() {
        var i = new Python.instance;
        i.__repr__ = function(obj) {return '42';};

        self.assert.equal(string(i), '42');
    }

    function call_class() {
        var i = new Python.instance;

        i.__call__ = function(){return 42;};

        self.assert.equal(i(), 42);
    }

    function call_instance() {
        var c = new Python.instance;
        var i = new Python.instance;

        c.__getattribute__ = function(obj, key) {
            return obj.__dict__['__class__'].__dict__[key];
        };
        c.__call__ = function(){return 42;};
        
        i.__class__ = c;

        self.assert.equal(i(), 42);
    }
}

function main() {
    using Rosella.Test.test;
    test(class instance);
}

// vim:set filetype=winxed:
