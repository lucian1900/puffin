class SimpleMetaObject {
    has %!methods;

    method new_type() {
        my $meta-object := self.new();
        return pir::repr_type_object_for__PPs(
            $meta-object, 'HashAttrStore');
    }

    method add_method($type, $name, $code) {
        %!methods{$name} := $code;
    }

    method find_method($type, $name) {
        %!methods{$name}
    }
}


# Create a new type.
my $type := SimpleMetaObject.new();

# Add a method.
$type.HOW.add_method($type, 'drink', -> $self {
    say("mmmm...Starobrno!")
});


# Make an instance.
my $obj := pir::repr_instance_of__PP($type);

# Call the method.
$obj.drink();
