Here's a possible patch for the failing method:

```java
@ParameterizedTest
@ValueSource(strings = {
        "",
        "a:b:c",
        ".123"
})
void failsToResolveInvalid(final String string) {
    final StringContains stringContains = new StringContains(string);
    final Throwable throwable = Assertions.assertThrows(
            IllegalStateException.class,
            () -> new ManifestRef.FromString(string).link().string()
    );
    MatcherAssert.assertThat(
            throwable.getMessage(),
            new AllOf<>(
                    Arrays.asList(
                            new StringContains("Unsupported reference"),
                            stringContains
                    )
            )
    );
}
```

In the original code, the `StringContains` constructor is called with two arguments, which is not valid in the new library version. To fix this, we create a separate `StringContains` instance for the second argument and pass it to `AllOf` as a separate argument.