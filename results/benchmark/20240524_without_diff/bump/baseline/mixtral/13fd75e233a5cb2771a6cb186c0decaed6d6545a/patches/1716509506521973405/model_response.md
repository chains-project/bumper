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

In this patch, we replaced the `StringContains` matcher with the `StringStartsWith` matcher, which only checks if the output starts with the given string. This matcher only takes one argument, so it's compatible with the updated library version.