Here's a fixed version of the `failsToResolveInvalid` method that should resolve the error:

```java
@ParameterizedTest
@ValueSource(strings = {
        "",
        "a:b:c",
        ".123"
})
void failsToResolveInvalid(final String string) {
    final HamcrestMatcher stringContains = StringContains.containsString(string);
    final Throwable throwable = Assertions.assertThrows(
            IllegalStateException.class,
            () -> new ManifestRef.FromString(string).link().string()
    );
    MatcherAssert.assertThat(
            throwable.getMessage(),
            new AllOf<>(
                    Arrays.asList(
                            new StringContains(true, "Unsupported reference"),
                            stringContains
                    )
            )
    );
}
```

In this version, I created a new variable `stringContains` to store the `StringContains` matcher that takes only one argument, as required by the updated library version. This avoids the error caused by passing two arguments to the constructor.