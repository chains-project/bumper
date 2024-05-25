Here's a possible patch for the failing client code:

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

The only change made is to replace `new StringContains` with `CoreMatchers.stringContains`. This is because the constructor for `StringContains` has been removed in the version of Hamcrest being used. Instead, the `stringContains` method from `CoreMatchers` can be used.