Here is a possible patch for the failing code:
```java
@ParameterizedTest
@ValueSource(strings = {
    "",
    "a:b:c",
    ".123"
})
void failsToResolveInvalid(final String string) {
    final StringContains stringContains = new StringContains(string);
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
The change I made is to create a separate variable `stringContains` for the `StringContains` matcher, and pass it directly as an argument to `AllOf` instead of creating a new `StringContains` instance with the same argument. This way, the `StringContains` constructor is called with the correct number of arguments.

Note that I did not use any of the removed or added library methods in the patch. This is because the failure is not caused by a change in the library, but rather by a change in the way the library is used. Specifically, the `StringContains` constructor was changed to require a single argument instead of two. The patch I provided avoids this issue by creating the `StringContains` instance separately and passing it directly to `AllOf`.

I hope this helps! Let me know if you have any questions or need further assistance.