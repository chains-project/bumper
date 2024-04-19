Here's the updated `failsToResolveInvalid` method that should fix the error:

```java
@ParameterizedTest
@ValueSource(strings = {
        "",
        "a:b:c",
        ".123"
})
void failsToResolveInvalid(final String string) {
    final HamcrestMatcher<String> stringContains =
            new StringContains<>(string);
    final HamcrestMatcher<IllegalStateException> illegalStateExceptionMatcher =
            new AllOf<>(Arrays.asList(
                    new StringContains<>(true, "Unsupported reference"),
                    stringContains
            ));
    final Throwable throwable = Assertions.assertThrows(
            IllegalStateException.class,
            () -> new ManifestRef.FromString(string).link().string()
    );
    MatcherAssert.assertThat(throwable, illegalStateExceptionMatcher);
}
```

In this updated version, I created two local variables `stringContains` and `illegalStateExceptionMatcher` to hold the `StringContains` and `AllOf` matchers respectively. This way, the matchers can be constructed with the correct number of arguments.