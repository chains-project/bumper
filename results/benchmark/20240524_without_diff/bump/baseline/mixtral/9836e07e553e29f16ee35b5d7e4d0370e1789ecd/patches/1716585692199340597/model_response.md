Here is a possible patch for the failing client code:

```java
@Test
void shouldPull() throws Exception {
    final String image = this.copy(new Image.ForOs());
    this.cli.run("push", image);
    this.cli.run("image", "rm", image);
    final String output = this.cli.run("pull", image);
    MatcherAssert.assertThat(
        output,
        CoreMatchers.stringContains(
            String.format("Status: Downloaded newer image for %s", image)
        )
    );
}
```

In this patch, I replaced the `StringContains` class with the `CoreMatchers.stringContains` method, which is an added library method identified with `++`. This should fix the error message and allow the test to pass.