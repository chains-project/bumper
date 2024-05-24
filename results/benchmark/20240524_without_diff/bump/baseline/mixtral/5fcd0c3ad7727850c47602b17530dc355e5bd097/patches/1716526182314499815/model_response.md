Here's a possible patch for the code:

```java
import org.pitest.classinfo.ClassInfo;
import org.pitest.classinfo.ClassInfoBuilder;
import org.pitest.classinfo.ClassName;
import org.pitest.coverage.BlockStore;
import org.pitest.coverage.CodeCoverage;
import org.pitest.coverage.Store;
import java.util.Arrays;
import java.util.Collection;
import java.util.stream.Collectors;

private MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final ClassMutationResults data) {
    CodeCoverage codeCoverage = coverage.get(data.getMutatedClass());
    Store store = codeCoverage.getStore();
    BlockStore blockStore = store.getBlockStore();
    Collection<ClassInfo> classInfos = blockStore.getBlockEntries().stream()
            .filter(entry -> entry.getClassName().equals(data.getMutatedClass()))
            .flatMap(entry -> Arrays.stream(entry.getBlocks()))
            .map(block -> ClassInfoBuilder.forClass(ClassName.fromString(data.getMutatedClass())))
            .collect(Collectors.toList());
    return new MutationTestSummaryData(data.getFileName(),
            data.getMutations(), classInfos);
}
```

This patch changes the way the `ClassInfo` objects are obtained. Instead of using the `getClassInfo` method from `CoverageDatabase`, it uses the `BlockStore` from the `CodeCoverage` object. It then filters the blocks for the specific class, builds `ClassInfo` objects for each block, and collects them into a list. This should work as a replacement for the original code.