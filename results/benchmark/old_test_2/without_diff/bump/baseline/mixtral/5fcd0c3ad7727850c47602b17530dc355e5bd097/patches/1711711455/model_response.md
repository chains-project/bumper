Here is a proposed patch for the failing client code:

```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    Set<String> mutatedClass = Collections.singleton(data.getMutatedClass());
