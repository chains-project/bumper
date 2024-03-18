```java
    void shouldPull() throws Exception {
        final String image = this.copy(new Image.ForOs());
        this.cli.run("push", image);
        this.cli.run("image", "rm", image);
        final String output = this.cli.run("pull", image);
        MatcherAssert.assertThat(
            output,
            new StringContains(
                false,
                "Status: Downloaded newer image for %s".formatted(image)
            )
        );
    }
```