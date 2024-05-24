Here's a possible patch for the failing client code:

```java
@Test
void shouldPush() throws Exception {
    final Image original = new Image.ForOs();
    final String image = this.copy(original);
    final String output = this.cli.run("push", image);
    MatcherAssert.assertThat(
        output,
        new StringStartsWith(
            String.format("latest: digest: %s", original.digest())
        )
    );
}
```

In this patch, we replaced `StringContains` with `StringStartsWith` to match the new library version. The `StringStartsWith` matcher checks if a string starts with a given substring, which is what the original code intended to do.