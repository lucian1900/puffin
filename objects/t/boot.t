$load 'rosella/test.pbc';
$load 'puffin/builtins.pbc';

class boot {
    function builtins_call() {
        self.assert.throws_nothing(function(){
            using Python.builtins;
            builtins();
        });
    }

    function check_object() {
        using Python.builtins;

        var env = builtins();
        var object = env['object'];

        self.assert.equal(object.__name__, 'object');
    }

    function globalize() {
        using Python.builtins;
        using Python.globalize;
        using Python.id;

        var env = builtins();
        globalize(env);

        var object;
        ${ get_global object, 'object' };

        self.assert.equal(id(env['object']), id(object));
    }
}

function main() {
    using Rosella.Test.test;
    test(class boot);
}
