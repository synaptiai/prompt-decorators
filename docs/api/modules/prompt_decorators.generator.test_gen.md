# Module `prompt_decorators.generator.test_gen`

Test Generator for Prompt Decorators.
This module generates comprehensive unit tests for all decorators defined in the registry.
It creates test cases for:
1. Decorator initialization with valid and invalid parameters
2. Parameter validation
3. Apply method functionality
4. Serialization/deserialization
5. Compatibility checks

The generated tests follow pytest conventions and can be run with standard pytest commands.

## Classes

- [`Parameter`](#class-parameter): Parameter class for test generation.
- [`TestGenerator`](#class-testgenerator): Generator for decorator unit tests.

### Class `Parameter`

Parameter class for test generation.

#### Methods

- `__init__(name, type=string, required=False, validation, schema, enum, description)`

### Class `TestGenerator`

Generator for decorator unit tests.

#### Methods

- `__init__(registry_dir, output_dir, template_dir)`
- `generate_all_tests() -> typing.List[str]`
- `generate_conftest() -> <class 'str'>`
- `generate_decorator_test(decorator_data) -> typing.Optional[str]`
- `generate_test_discovery() -> <class 'str'>`

## Functions

- [`main`](#function-main): Run the test generator as a standalone script.

### Function `main`

**Signature:** `main()`

Run the test generator as a standalone script.
