```java
@Test
    void shouldPull() throws Exception {
        final String image = this.copy(new Image.ForOs());
        this.cli.run("push", image);
        this.cli.run("image", "rm", image);
        final String output = this.cli.run("pull", image);
        final String[] lines = output.split("\n");
        final String lastLine = lines[lines.length - 1];
        MatcherAssert.assertThat(
            lastLine,
            new StringContains(
                false,
                String.format("Status: Downloaded newer image for %s", image)
            )
        );
    }
```