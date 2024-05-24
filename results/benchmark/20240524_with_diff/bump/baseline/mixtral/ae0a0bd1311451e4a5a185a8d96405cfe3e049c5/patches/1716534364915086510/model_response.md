Here's a possible patch that fixes the error:

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
                new AllOf<>(
                        Arrays.asList(
                                new StringContains(true, "Unsupported reference"),
                                stringContains
                        )
                )
        );
    }
```

In this patch, we create a `StringContains` matcher and pass it directly as an argument to `AllOf`, instead of wrapping it in a `new StringContains` expression. This avoids the compilation error caused by the change in the `StringContains` constructor.