Here's the proposed patch for the failing method:

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

The changes made include creating a variable for the `StringContains` matcher and using the `allOf` method from `AllOf` to combine the two matchers.