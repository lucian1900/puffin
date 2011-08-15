$load 'rosella/test.pbc';
$load 'puffin/builtins.pbc';

function excls() {
    using Python.type;
    using Python.object;
    using Python.exception;

    var t = type();
    var o = object(t);

    return exception(t, o);
}

class exception {
    function init() {
        var e = excls();
    }

    function throw() {
        var e = excls();

        self.assert.throws(function(){
            throw e.__value__;
        });
    }
}

function main() {
    using Rosella.Test.test;
    test(class exception);
}

// vim:set filetype=winxed:
