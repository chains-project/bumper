```java
import com.jcabi.aspects.Tv;

    public class MkGithub {

        private Tv tv = new Tv();

        public MkGithub() {
            // This constructor is needed to create an instance of MkGithub.
        }

        public void mock() {
            // This method is needed to mock the GitHub API.
            tv.play("https://github.com/");
        }
    }
```