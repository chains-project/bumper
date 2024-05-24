Here is a proposed patch for the failing client code:
```java
@ParameterizedTest
@ValueSource(strings = {
        "",
        "a:b:c",
        ".123"
})
void failsToResolveInvalid(final String string) {
    final HamcrestMatcher stringContains = new StringContains(string);
    final Throwable throwable = Assertions.assertThrows(
            IllegalStateException.class,
            () -> new ManifestRef.FromString(string).link().string()
    );
    MatcherAssert.assertThat(
            throwable.getMessage(),
            new AllOf<>(
                    Arrays.asList(
                            new StringStartsWith("Unsupported reference"),
                            stringContains
                    )
            )
    );
}
```
In this patch, I have created a variable `stringContains` to store the `StringContains` matcher. Instead of using `new StringContains(true, string)`, I have used `new StringContains(string)` to match the method signature of the `StringContains` constructor.

Additionally, I have replaced `new StringContains(true, "Unsupported reference")` with `new StringStartsWith("Unsupported reference")` to avoid using the removed `StringContains` constructor with a boolean argument.

With these changes, the client code should be able to compile and run successfully with the new library version.