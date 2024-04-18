Sure, here's a proposed patch to fix the error:

```java
@Test
void shouldPush() throws Exception {
    final Image original = new Image.ForOs();
    final String image = this.copy(original);
    final String output = this.cli.run("push", image);
    MatcherAssert.assertThat(
        output,
        new StringContains(original.digest())
    );
}
```

In this patch, I removed the `false` argument from the `StringContains` constructor, as it is no longer required and is causing the error. The `digest()` method of the `Image` class should still be available and can be used directly in the `StringContains` constructor.