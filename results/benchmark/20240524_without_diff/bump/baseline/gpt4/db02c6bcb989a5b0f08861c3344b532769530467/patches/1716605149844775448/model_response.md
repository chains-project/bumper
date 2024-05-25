```java
@Test
void shouldPull() throws Exception {
    final String image = this.copy(new Image.ForOs());
    this.cli.run("push", image);
    this.cli.run("image", "rm", image);
    final String output = this.cli.run("pull", image);
    MatcherAssert.assertThat(
        output,
        new org.hamcrest.CoreMatchers.Contains(
            String.format("Status: Downloaded newer image for %s", image)
        )
    );
}
```