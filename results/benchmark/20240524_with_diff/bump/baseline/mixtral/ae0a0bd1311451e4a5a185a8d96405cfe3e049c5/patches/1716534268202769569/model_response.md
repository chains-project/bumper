Here's the fixed version of the `failsToResolveInvalid` method:

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

The issue is caused by the incorrect usage of the `StringContains` constructor. Instead of passing `true` or `false` as the first argument, you should pass the expected substring. I created a variable `stringContainsMatcher` to store the `StringContains` matcher and passed it to the `AllOf.allOf` method. This way, the code now uses the `StringContains` constructor correctly and adheres to the new library version.