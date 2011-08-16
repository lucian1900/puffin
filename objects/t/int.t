$load 'rosella/test.pbc';
$load 'puffin/builtins.pbc';

function intcls() {
    using Python.type;
    using Python.object;
    using Python.int;

    var t = type();
    var o = object(t);

    return int(t, o);
}

class int {
    function boot() {
        self.assert.throws_nothing(function(){
            intcls();
        });
    }

    function create() {
        var i = intcls();
        var f = i.__new__;
    
        self.assert.equal(f(i, 2).__value__, 2);
    }

    function create_zero() {
        var i = intcls();
        var f = i.__new__;

        self.assert.equal(f(i).__value__, 0);
    }

    function create_one() {
        var i = intcls();

        var f = i.__new__;
        var a = f(i, 1);

        self.assert.equal(a.__value__, 1);
    }

    function repr() {
        var i = intcls();

        var f = i.__new__;
        var a = f(i, 1);

        f = i.__repr__;

        self.assert.equal(f(a), '1');
    }

    function add() {
        var i = intcls();

        var f = i.__new__;
        
        var a = f(i, 20); 
        var b = f(i, 22);

        var add = i.__add__;
        var r = add(a, b);
        self.assert.equal(r.__value__, 42);
    }
}

function main() {
    using Rosella.Test.test;
    test(class int);
}

// vim:set filetype=winxed:
