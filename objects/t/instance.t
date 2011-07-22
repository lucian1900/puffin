$load 'rosella/test.pbc';
$load 'puffin/builtins.pbc';

class instance {
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

    function getattribute() {
        var i = new Python.instance;
        i.__getattribute__ = function(obj, name) {
            return 42;
        };
        
        self.assert.equal(i.a, 42);
    }

    function call_func() {
        var i = new Python.instance;
        i.b = function(){return 42;};

        var func = i.b;
        self.assert.equal(func(), 42);
    }

    function call_func_attr() {
        var i = new Python.instance;
        i.f = function(a, b){return a + b;};

        var func = i.f;
        self.assert.equal(func(1, 2), 3);
    }

    function get_string() {
        var i = new Python.instance;
        i.__repr__ = function(obj) {return '42';};

        self.assert.equal(string(i), '42');
    }

    function call() {
        var i = new Python.instance;
        i.__call__ = function(){return 42;};

        self.assert.equal(i(), 42);
    }

    function get_mro() {
        self.status.unimplemented('writeme');
        using Python.get_mro;
    }
}

function main() {
    using Rosella.Test.test;
    test(class instance);
}

