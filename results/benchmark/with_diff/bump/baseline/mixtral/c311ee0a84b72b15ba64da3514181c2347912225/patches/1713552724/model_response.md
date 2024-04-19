Here's a fixed version of the `failsToResolveInvalid` method that should work with the updated library version:
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
                    new StringContains("Unsupported reference"),
                    new StringContains(string)
            )
    );
}
```
The only change I made is to remove the `true` and `false` arguments from the first and second `StringContains` matchers, respectively. This is because the updated library version no longer accepts those arguments.