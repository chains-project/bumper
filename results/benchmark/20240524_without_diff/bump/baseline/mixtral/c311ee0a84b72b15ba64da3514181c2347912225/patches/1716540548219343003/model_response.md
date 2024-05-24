Here's a potential patch for the failing code:

```java
    @ParameterizedTest
    @ValueSource(strings = {
            "",
            "a:b:c",
            ".123"
    })
    void failsToResolveInvalid(String string) {
        final Throwable throwable = Assertions.assertThrows(
                IllegalStateException.class,
                () -> new ManifestRef.FromString(string).link().string()
        );
        MatcherAssert.assertThat(
                throwable.getMessage(),
                new AllOf<>(
                        Arrays.asList(
                                new StringContains("Unsupported reference"),
                                new StringContains(string)
                        )
                )
        );
    }
```

The only change made is to remove the `true` and `false` arguments from the `StringContains` constructor calls. The `StringContains` constructor now only takes a single argument, a `String` to match. This is based on the error message, which indicates that the constructor is now expected to take a single argument.