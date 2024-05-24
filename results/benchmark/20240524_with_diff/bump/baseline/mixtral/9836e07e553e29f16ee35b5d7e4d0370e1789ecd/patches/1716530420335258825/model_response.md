Here's the proposed patch to fix the error:

```java
@Test
void shouldPush() throws Exception {
    final Image original = new Image.ForOs();
    final String image = this.copy(original);
    final String output = this.cli.run("push", image);
    MatcherAssert.assertThat(
        output,
        new StringContains(
            String.format("latest: digest: %s", original.digest())
        )
    );
}
```

In this patch, I removed the `false` argument from the `StringContains` constructor, since it is no longer required in the new library version. This should fix the error and allow the test to pass.