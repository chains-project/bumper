Here's a proposed patch to fix the error:

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
            AllOf.allOf(
                    new StringContains("Unsupported reference"),
                    stringContains
            )
    );
}
```

In this patch, I created a new variable `stringContains` to store the `StringContains` matcher, and used the `allOf` method from `AllOf` to specify the matchers that should be satisfied. This way, the `StringContains` constructor is called with the correct number of arguments.