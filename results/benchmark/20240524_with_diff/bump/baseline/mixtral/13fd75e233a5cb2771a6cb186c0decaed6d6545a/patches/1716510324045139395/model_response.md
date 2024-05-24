Here's the fixed `failsToResolveInvalid` method:

```java
@ParameterizedTest
@ValueSource(strings = {
        "",
        "a:b:c",
        ".123"
})
void failsToResolveInvalid(final String string) {
    final HamcrestMatcher stringContains = StringContains.stringContains(string);
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

The fix involves creating a separate `StringContains` Hamcrest matcher for the input string, and then using it in the `AllOf.allOf` call. This way, the `StringContains` constructor will receive the correct number of arguments.