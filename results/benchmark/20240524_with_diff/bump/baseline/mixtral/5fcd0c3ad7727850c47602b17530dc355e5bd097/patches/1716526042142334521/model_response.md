Here's the proposed patch for the failing client code:

```java
import org.pitest.classinfo.ClassInfo;
import org.pitest.classinfo.ClassInfoBuilder;
import org.pitest.classinfo.ClassName;
import org.pitest.coverage.CoverageDatabase;
import org.pitest.coverage.CoverageInfo;
import org.pitest.coverage.CoverageResult;
import org.pitest.coverage.ReportCoverage;
import org.pitest.mutationtest.MutationResult;
import org.pitest.mutationtest.engine.gregor.MutationResultCode;
import org.pitest.util.Pair;

private MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final MutationResult data) {
    ClassName className = data.getMutatedClass();
    byte[] classBytecode = data.getMutatedClassBytecode();
    long timestamp = data.getMutationResultCode() == MutationResultCode.MUTATION_SURVIVED ? data.getTimestamp() : -1;

    ClassInfo classInfo = ClassInfoBuilder.forClass(className).addClassname(className.toString()).addClassFile(classBytecode).build();
    CoverageInfo coverageInfo = coverage.getCoverage(className);
    CoverageResult coverageResult = new CoverageResult(coverageInfo, className);
    ReportCoverage reportCoverage = new ReportCoverage() {
        @Override
        public CoverageResult getCoverage(ClassName className) {
            return coverageResult;
        }
    };

    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(),
        ClassInfoVisitor.getClassInfo(className, classBytecode, timestamp, reportCoverage));
}
```

This patch creates a `ClassInfo` instance using the new `ClassInfoBuilder` method, and it creates a `CoverageResult` instance to pass to the `ClassInfoVisitor.getClassInfo` method. The `ReportCoverage` instance is a simple implementation of the `ReportCoverage` interface that returns the `CoverageResult` instance for the given class name.