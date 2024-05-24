Here's a possible patch for the failing client code:

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
                            new StringStartsWith(string)
                    )
            )
    );
}
```

In this patch, I replaced the `StringContains` matcher with the `StringStartsWith` matcher, which is a new method added in the library. This matcher checks if the given string starts with the expected substring, which should work for this test case.

Note that I used `StringStartsWith` instead of `StringContains`, because the latter expects a single string argument, while the former expects a boolean argument followed by a string argument, which is not compatible with the library version used in the original code.

Also, note that I removed the second argument of `StringContains`, because it is not used in the original code, and it causes a compilation error in the new library version.