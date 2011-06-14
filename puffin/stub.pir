.sub initial_load_bytecode :anon :load :init
    load_bytecode 'boot.pbc'
.end

.sub '__main__' :main
    .local pmc env
    .local pmc builtins
    get_hll_global boot, ['Python'], 'builtins'
    env = builtins()
    .local pmc obj
    obj = env['object']
.end
