$load 'rosella/test.pbc';
$load 'puffin/builtins.pbc';

function tupcls() {
    using Python.type;
    using Python.object;
    using Python.tuple;

    var t = type();
    var o = object(t);

    return tuple(t, o);
}


class tuple {
    function boot() {
        self.assert.throws_nothing(function(){
            tupcls();
        });
    }

    function create() {
        var t = tupcls();
        var f = t.__new__;

        self.assert.equal(f(t).__value__, []);
    }

    function create_arr() {
        var t = tupcls();
        var f = t.__new__;

        self.assert.equal(f(t, [1, 2, 3]).__value__, [1, 2, 3]);
    }

    function getitem() {
        var t = tupcls();

        var f = t.__new__;
        var i = f(t, [1, 2, 3]);

        var get = t.__getitem__; 
        self.assert.equal(get(i, 1), 2);
    }

    function len() {
        var t = tupcls();

        var f = t.__new__;
        var i = f(t, [1, 2, 3]);

        var len = t.__len__; 
        self.assert.equal(len(i), 3);
    }
}

function main() {
    using Rosella.Test.test;
    test(class tuple);
}

// vim:set filetype=winxed:
