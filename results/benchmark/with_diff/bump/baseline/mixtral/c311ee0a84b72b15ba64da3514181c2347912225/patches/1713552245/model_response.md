Here's the fixed version of the `shouldPull` method:

```java
@Test
void shouldPull() throws Exception {
    final String image = this.copy(new Image.ForOs());
    this.cli.run("push", image);
    this.cli.run("image", "rm", image);
    final String output = this.cli.run("pull", image);
    MatcherAssert.assertThat(
        output,
        new StringContains(String.format("Status: Downloaded newer image for %s", image))
    );
}
```

The issue was caused by an incorrect usage of the `StringContains` constructor. I removed the `false` argument, so now the constructor call matches the expected argument list.