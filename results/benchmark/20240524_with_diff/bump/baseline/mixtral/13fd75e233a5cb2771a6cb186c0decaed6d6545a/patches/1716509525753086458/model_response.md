Here's the proposed patch for the failing method:

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

In this patch, I replaced the `StringContains` matcher with the `StringStartsWith` matcher, which only takes a single argument. This change fixes the error message, which indicates that the `StringContains` constructor is expecting a single argument, but received two.