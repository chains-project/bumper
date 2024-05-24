Here is the proposed patch:

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

In this patch, I created a variable `stringContains` to store the `StringContains` matcher, and passed the `string` argument directly to the `StringContains` constructor. This should fix the error caused by the change in the library version.