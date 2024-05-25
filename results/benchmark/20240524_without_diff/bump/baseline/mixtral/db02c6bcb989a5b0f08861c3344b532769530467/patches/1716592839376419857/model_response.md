Here is a fixed version of the `shouldPull` method:

```java
@Test
void shouldPull() throws Exception {
    final String image = this.copy(new Image.ForOs());
    this.cli.run("push", image);
    this.cli.run("image", "rm", image);
    final String output = this.cli.run("pull", image);
    MatcherAssert.assertThat(
        output,
        CoreMatchers.stringContainsString(
            String.format("Status: Downloaded newer image for %s", image)
        )
    );
}
```

The only change made is to replace the `new StringContains` constructor with `CoreMatchers.stringContainsString`. This is because the `StringContains` constructor has been removed in the version of Hamcrest being used. `CoreMatchers.stringContainsString` is a new method that has been added in the version of Hamcrest being used and can be used as a replacement.