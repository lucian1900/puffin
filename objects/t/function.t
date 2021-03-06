$load 'rosella/test.pbc';
$load 'puffin/builtins.pbc';

function funccls() {
    using Python.type;
    using Python.object;
    using Python.func;

    var t = type();
    var o = object(t);

    return func(t, o);
}

class func {
    function boot() {
        self.assert.throws_nothing(function(){
            funccls(); 
        });
    }

    function create() {
        var fn = funccls();
        var f = fn.__new__;

        var code = function() {};
        var i = f(fn, code);

        using Python.id;
        self.assert.equal(id(i.__call__), id(code));
    }

    function call() {
        var fn = funccls();
        var f = fn.__new__;

        var i = f(fn, function(){return 42;});

        self.assert.equal(i(), 42);
    }

    function call_args() {
        var fn = funccls();
        var f = fn.__new__;

        var i = f(fn, function(a){return a+1;});

        self.assert.equal(i(41), 42);
    }

    function method_get() {
        var fn = funccls();
        var f = fn.__new__;
        var i = f(fn, function(a){return a+1;});
    
        f = fn.__get__;
        var b = f(i, 41, null);

        self.assert.equal(b(), 42); 
    }
}

function main() {
    using Rosella.Test.test;
    test(class func);
}

// vim:set filetype=winxed:
