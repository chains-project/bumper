Here's a fixed version of the `failsToResolveInvalid` method that should resolve the error:

```java
@ParameterizedTest
@ValueSource(strings = {
        "",
        "a:b:c",
        ".123"
})
void failsToResolveInvalid(final String string) {
    final HamcrestMatcher<String> matcher = new StringContains(string);
    final Throwable throwable = Assertions.assertThrows(
            IllegalStateException.class,
            () -> new ManifestRef.FromString(string).link().string()
    );
    MatcherAssert.assertThat(
            throwable.getMessage(),
            new AllOf<>(
                    Arrays.asList(
                            new StringContains("Unsupported reference"),
                            matcher
                    )
            )
    );
}
```

The change here is to create a separate `matcher` variable for the `StringContains` matcher, and pass that variable as an argument to the `AllOf` constructor. This avoids passing the `true` or `false` boolean arguments that were causing the error.