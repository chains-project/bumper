```java
package com.jcabi.aspects;

import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.DeclareParents;

@Aspect
public class TvAspect {

    @DeclareParents(value = "com.jcabi.ssh.SshByPassword+", defaultImpl = TvImpl.class)
    public static Tv tv;

}
```