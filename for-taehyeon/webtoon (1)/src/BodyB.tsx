import { FunctionComponent, useCallback } from "react";
import styles from "./css/BodyB.module.css";

export const BodyB: FunctionComponent = () => {
  const onGroupContainerClick = useCallback(() => {
    window.open(
      "https://www.figma.com/file/2P3p4u9jLwLlTIpHbhbO3t/?node-id=66%3A38"
    );
  }, []);

  const onGroupContainer1Click = useCallback(() => {
    window.open(
      "https://www.figma.com/file/2P3p4u9jLwLlTIpHbhbO3t/?node-id=66%3A38"
    );
  }, []);

  const onGroupContainer2Click = useCallback(() => {
    window.open(
      "https://www.figma.com/file/2P3p4u9jLwLlTIpHbhbO3t/?node-id=66%3A38"
    );
  }, []);

  const onGroupContainer3Click = useCallback(() => {
    window.open(
      "https://www.figma.com/file/2P3p4u9jLwLlTIpHbhbO3t/?node-id=66%3A38"
    );
  }, []);

  return (
    <div className={styles.bodyBDiv}>
      <div className={styles.groupDiv} onClick={onGroupContainerClick}>
        <b className={styles.b}>웹툰 작품명</b>
        <div className={styles.div}>작가명</div>
        <div className={styles.buttonDiv}>
          <div className={styles.rectangleDiv} />
          <div className={styles.learnMoreDiv}>키워드 1</div>
        </div>
        <div className={styles.div2}>
          <div className={styles.rectangleDiv} />
          <div className={styles.learnMoreDiv1}>키워드 2</div>
        </div>
        <div className={styles.div3}>
          <div className={styles.rectangleDiv2} />
          <div className={styles.div4}>플랫폼</div>
        </div>
        <div className={styles.div5} />
      </div>
      <div className={styles.groupDiv1} onClick={onGroupContainer1Click}>
        <b className={styles.b}>웹툰 작품명</b>
        <div className={styles.div}>작가명</div>
        <div className={styles.buttonDiv}>
          <div className={styles.rectangleDiv} />
          <div className={styles.learnMoreDiv}>키워드 1</div>
        </div>
        <div className={styles.div2}>
          <div className={styles.rectangleDiv} />
          <div className={styles.learnMoreDiv1}>키워드 2</div>
        </div>
        <div className={styles.div3}>
          <div className={styles.rectangleDiv2} />
          <div className={styles.div4}>플랫폼</div>
        </div>
        <div className={styles.div5} />
      </div>
      <div className={styles.groupDiv2} onClick={onGroupContainer2Click}>
        <b className={styles.b}>웹툰 작품명</b>
        <div className={styles.div}>작가명</div>
        <div className={styles.buttonDiv}>
          <div className={styles.rectangleDiv} />
          <div className={styles.learnMoreDiv}>키워드 1</div>
        </div>
        <div className={styles.div2}>
          <div className={styles.rectangleDiv} />
          <div className={styles.learnMoreDiv1}>키워드 2</div>
        </div>
        <div className={styles.div3}>
          <div className={styles.rectangleDiv2} />
          <div className={styles.div4}>플랫폼</div>
        </div>
        <div className={styles.div5} />
      </div>
      <div className={styles.groupDiv3} onClick={onGroupContainer3Click}>
        <b className={styles.b}>웹툰 작품명</b>
        <div className={styles.div}>작가명</div>
        <div className={styles.buttonDiv}>
          <div className={styles.rectangleDiv} />
          <div className={styles.learnMoreDiv}>키워드 1</div>
        </div>
        <div className={styles.div2}>
          <div className={styles.rectangleDiv} />
          <div className={styles.learnMoreDiv1}>키워드 2</div>
        </div>
        <div className={styles.div3}>
          <div className={styles.rectangleDiv2} />
          <div className={styles.div4}>플랫폼</div>
        </div>
        <div className={styles.div5} />
      </div>
      <div className={styles.div15}>
        <div className={styles.div16} />
        <div className={styles.div17}>검색단어</div>
      </div>
      <div className={styles.div18}>
        <p className={styles.p}>일단해보조</p>
        <p className={styles.p1}>웹툰 통합플랫폼</p>
      </div>
    </div>
  );
};
