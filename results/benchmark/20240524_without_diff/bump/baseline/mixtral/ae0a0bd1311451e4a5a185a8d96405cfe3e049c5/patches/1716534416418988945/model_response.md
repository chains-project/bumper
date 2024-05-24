Here's the updated `failsToResolveInvalid` method with the required changes:

```java
@ParameterizedTest
@ValueSource(strings = {
        "",
        "a:b:c",
        ".123"
})
void failsToResolveInvalid(final String string) {
    final HamcrestMatcher stringContainsMatcher = new StringContains(string);
    final Throwable throwable = Assertions.assertThrows(
            IllegalStateException.class,
            () -> new ManifestRef.FromString(string).link().string()
    );
    MatcherAssert.assertThat(
            throwable.getMessage(),
            AllOf.allOf(
                    new StringContains("Unsupported reference"),
                    stringContainsMatcher
            )
    );
}
```

The changes include:

1. Creating a `StringContains` Hamcrest matcher instance with the correct argument type (`string` instead of `false`).
2. Using the `allOf` method from `AllOf` to combine the two matchers.

These changes resolve the error related to the `StringContains` constructor and the mismatch in the number of arguments.