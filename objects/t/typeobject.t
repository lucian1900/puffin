$load 'rosella/test.pbc';
$load 'puffin/builtins.pbc';

function boot() {
    using Python.type;
    using Python.object;

    var t = type();
    var o = object(t);

    return t, o;
}

class type {

    function boot() {
        self.assert.throws_nothing(function(){
            :(var t, var o) = boot();
        });
    }

    function bases() {
        :(var t, var o) = boot();
        for(var i in t.__dict__) say(i);

        self.assert.equal(o.__dict__['__bases__'], []);
        self.assert.equal(t.__dict__['__bases__'], [o]);
    }

    function get_mro() {
        :(var t, var o) = boot();

        using Python.get_mro;
        //for(var i in get_mro(t)) say(string(i));

        self.assert.equal(get_mro(t), [t, o]);
        self.assert.equal(get_mro(o), [o]);
    }

    function set_attr() {
        :(var t, var o) = boot();
	
        o.a = 42;
        self.assert.equal(o.__dict__['a'], 42);
    }

    function get_attr() {
        :(var t, var o) = boot();

        o.a = 42;
        self.assert.equal(o.a, 42);
    }


    function type_init() {
        :(var t, var o) = boot();

        self.assert.throws_nothing(function(){
            t.__init__(t);
        });
    }

    function type_class() {
        :(var t, var o) = boot();

        self.assert.same(t.__class__, t);
    }
    
 
    function object_class() {
        :(var t, var o) = boot();

        self.assert.same(o.__class__, t);
    }

    function type_name() {
        :(var t, var o) = boot();

        self.assert.equal(t.__name__, 'type');
    }

    function object_name() {
        :(var t, var o) = boot();

        self.assert.equal(o.__name__, 'object');
    }

    function type_repr() {
        :(var t, var o) = boot();

        self.assert.equal(string(t), "<class 'type'>");
    }

    function object_repr() {
        :(var t, var o) = boot();
        
        self.assert.equal(string(o), "<class 'object'>");
    }

    function object_get() {
        :(var t, var o) = boot();

        self.assert.same(o.__repr__, o.__dict__['__repr__']);
    }

    function object_get_class() {
        :(var t, var o) = boot();

        self.assert.same(o.__hash__, t.__dict__['__hash__']);
    }

    function object_new() {
        :(var t, var o) = boot();
        
        var i = o.__new__(o);

        self.assert.same(i.__class__, o);
    }

    function instance_create() {
        :(var t, var o) = boot();

        var i = o();
        
        self.assert.same(i.__class__, o); // it's t instead of o for some reason
    }
        
    function instance_get() {
        :(var t, var o) = boot();

        var i = o.__new__(o);

        o.bla = 42;

        say(i.bla == null);
        self.assert.same(i.bla, o.__dict__['bla']);
    }

    function instance_class_get() {
        :(var t, var o) = boot();

        var i = o.__new__(o);

        t.bla = 42;

        self.assert.same(i.bla, t.__dict__['bla']);
    }

    function type_set_attr() {
        :(var t, var o) = boot();

        o.foo = 'bar';
        self.assert.equal(o.foo, 'bar');
    }

    function instance_set_attr() {
        :(var t, var o) = boot();

        var i = o.__new__(o);
        i.foo = 'bar';

        self.assert.equal(i.foo, 'bar');
    }

    function non_data_descriptor() {
        :(var t, var o) = boot();

        var i = o.__new__(o);
        i.__get__ = function(obj, attr) {return 42;};
        t.i = i;

        self.assert.equal(t.i, 42);
    }
}

function main() {
    using Rosella.Test.test;
    test(class type);
}

// vim:set filetype=winxed:
