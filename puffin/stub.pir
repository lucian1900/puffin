.sub initial_load_bytecode :anon :load :init
    load_bytecode 'boot.pbc'
.end

.sub '__main__' :main
    .local pmc builtins
    get_global builtins, ['Python'], 'builtins'

    .local pmc env
    env = builtins()

    .local pmc obj
    obj = env['object']
.end
