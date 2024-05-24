Here is the proposed patch:
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
                                new StringStartsWith("Unsupported reference"),
                                stringContains
                        )
                )
        );
    }
```
Explanation:
- The `StringContains` constructor now requires only one argument, so I created a variable `stringContains` to store the matcher.
- I changed the `StringContains` constructor argument to the `string` parameter of the test method.
- I changed the `StringContains` constructor argument to a `StringStartsWith` matcher, since the error message must start with "Unsupported reference".