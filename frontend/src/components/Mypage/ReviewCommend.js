import React from 'react';
function ReviewCommend({ reviewCommentData }) {
  console.log(reviewCommentData);
  return (
    <div className="ReviewListContainer">
      <div className="Reviewtitle">작성한 댓글 목록</div>
      <div className="ReviewWrap">
        <div className="ListTitle">
          <div className="headRegion">댓글내용</div>
          <div className="headtitle">작성자</div>
          <div className="headtime">작성일자</div>
        </div>
        {reviewCommentData.map((data, key) => {
          return (
            <div key={key} className="item">
              <div className="region">{data.content}</div>
              <div className="textTitle">{data.user.username}</div>
              <div className="time">{data.created}</div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
export default ReviewCommend;