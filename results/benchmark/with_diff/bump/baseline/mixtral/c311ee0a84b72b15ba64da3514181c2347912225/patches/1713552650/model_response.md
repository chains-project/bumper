Here's a possible patch for the failing method:

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
                    Arrays.asList(
                            new StringContains("Unsupported reference"),
                            new StringStartsWith(string)
                    )
            )
    );
}
```

In this patch, I replaced the `StringContains` matcher with a `StringStartsWith` matcher, which has the same effect of checking if the message starts with the given string, but has the correct signature. I also removed the second argument of `StringContains`, since it's not needed in this case.