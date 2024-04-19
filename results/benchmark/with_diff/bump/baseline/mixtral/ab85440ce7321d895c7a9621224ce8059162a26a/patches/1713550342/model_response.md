Here's the fixed version of the `failsToResolveInvalid` method:

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
                            new StringContains("Unsupported reference"),
                            new IsEqualIgnoringCase(string)
                    )
            )
    );
}
```

The changes include:

1. Replacing `new StringContains(false, string)` with `new IsEqualIgnoringCase(string)` to use the new `IsEqualIgnoringCase` matcher, which was added in the new library version.
2. Fixing the `StringContains` constructor by removing the `boolean` argument. This was causing the error message you encountered.

The `IsEqualIgnoringCase` matcher is used to check if the input string is equal to the expected string, ignoring the case. This should work similarly to the original `StringContains` matcher, but without the additional `boolean` argument.