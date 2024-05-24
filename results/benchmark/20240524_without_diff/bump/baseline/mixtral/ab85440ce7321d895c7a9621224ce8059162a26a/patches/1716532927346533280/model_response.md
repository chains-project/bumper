Here is a possible patch for the failing client code:
```java
@ParameterizedTest
@ValueSource(strings = {
    "",
    "a:b:c",
    ".123"
})
void failsToResolveInvalid(final String string) {
    final Throwable throwable = Assertions.assertThrows(
        IllegalStateException.class,
        () -> new ManifestRef.FromString(string).link().string()
    );
    MatcherAssert.assertThat(
        throwable.getMessage(),
        new AllOf<>(
            Arrays.asList(
                new StringStartsWith(String.format("%s: ", string)),
                new StringContains("Unsupported reference")
            )
        )
    );
}
```
In this patch, I replaced the `StringContains` matcher with two new matchers: `StringStartsWith` and `StringContains`. The `StringStartsWith` matcher checks if the input string starts with the given prefix, and the `StringContains` matcher checks if the input string contains the given substring.

I used the `String.format` method to dynamically generate the prefix for the `StringStartsWith` matcher based on the input string. This allows me to check if the error message starts with the input string followed by a colon and a space, as required by the updated library version.

Note that I did not remove the `@Override` decorator from the method, as it is still overriding a method in the new version of the library.