```java
import org.apache.maven.project.MavenProject;
import org.apache.maven.project.MavenProjectHelper;
import org.apache.maven.shared.dependency.graph.DependencyGraph;
import org.apache.maven.shared.dependency.graph.DependencyNode;
import org.apache.maven.shared.dependency.graph.traversal.DependencyNodeVisitor;
import org.apache.maven.shared.dependency.graph.traversal.GraphTraversal;
import org.apache.maven.shared.dependency.graph.traversal.PostOrderDependencyNodeVisitor;
import org.apache.maven.shared.dependency.graph.traversal.TraversalVisitor;
import org.apache.maven.shared.dependency.graph.traversal.VisitorNode;
```